import yaml
import logging
from api_gen.schema import Schema
from api_gen.helpers import get_all_tags
from api_gen.api import Api
from pathlib import Path
logger = logging.getLogger(__name__)


def generate_api(input_path: str = "openapi.yaml", output_path: str = "api_tools"):

    with open(input_path, "r") as f:
        yaml_data = yaml.safe_load(f)

    schema = Schema(yaml_data["components"]["schemas"])
    schema.generate_schemas()

    query_schema_params = []
    for tag in get_all_tags(yaml_data["paths"]):
        api = Api(
            yaml_data["paths"],
            base_url=yaml_data.get(
                "servers", [{"url": "http://localhost:8080"}])[0]["url"],
            only_tag=tag,
        )

        api.generate_apis(schema_path=output_path+".schema",
                          client_kind="async")  # type: ignore
        query_schema_params.extend(api.query_param_schemas)

        api.write_api(output_path)

    schema.write_to_file(output_path, query_schema_params)
