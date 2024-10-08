import os
import tempfile
from pathlib import Path

import airflow
from airflow.configuration import conf
from airflow.version import version as airflow_version
from packaging.version import Version

from cosmos.constants import DEFAULT_COSMOS_CACHE_DIR_NAME, DEFAULT_OPENLINEAGE_NAMESPACE

# In MacOS users may want to set the envvar `TMPDIR` if they do not want the value of the temp directory to change
DEFAULT_CACHE_DIR = Path(tempfile.gettempdir(), DEFAULT_COSMOS_CACHE_DIR_NAME)
cache_dir = Path(conf.get("cosmos", "cache_dir", fallback=DEFAULT_CACHE_DIR) or DEFAULT_CACHE_DIR)
enable_cache = conf.getboolean("cosmos", "enable_cache", fallback=True)
enable_cache_partial_parse = conf.getboolean("cosmos", "enable_cache_partial_parse", fallback=True)
enable_cache_package_lockfile = conf.getboolean("cosmos", "enable_cache_package_lockfile", fallback=True)
enable_cache_dbt_ls = conf.getboolean("cosmos", "enable_cache_dbt_ls", fallback=True)
rich_logging = conf.getboolean("cosmos", "rich_logging", fallback=False)
dbt_docs_dir = conf.get("cosmos", "dbt_docs_dir", fallback=None)
dbt_docs_conn_id = conf.get("cosmos", "dbt_docs_conn_id", fallback=None)
dbt_docs_index_file_name = conf.get("cosmos", "dbt_docs_index_file_name", fallback="index.html")
enable_cache_profile = conf.getboolean("cosmos", "enable_cache_profile", fallback=True)
dbt_profile_cache_dir_name = conf.get("cosmos", "profile_cache_dir_name", fallback="profile")

try:
    LINEAGE_NAMESPACE = conf.get("openlineage", "namespace")
except airflow.exceptions.AirflowConfigException:
    LINEAGE_NAMESPACE = os.getenv("OPENLINEAGE_NAMESPACE", DEFAULT_OPENLINEAGE_NAMESPACE)

AIRFLOW_IO_AVAILABLE = Version(airflow_version) >= Version("2.8.0")
