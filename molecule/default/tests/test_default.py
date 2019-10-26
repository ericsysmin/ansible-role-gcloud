import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


def test_hosts_file(host):
    f = host.file("/etc/hosts")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"


@pytest.mark.parametrize("command", [
    "bq",
    "docker-credential-gcloud",
    "gcloud",
    "git-credential-gcloud.sh",
    "gsutil"
])
def test_command_avail(host, command):
    """Check to see that command is in path"""

    assert host.exists(command)


@pytest.mark.parametrize("command", [
    "bq version",
    "gcloud -v",
    "gsutil version"
])
def test_command_exec(host, command):

    assert host.run_test(command)
