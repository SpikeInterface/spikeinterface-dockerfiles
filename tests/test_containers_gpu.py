import os
import shutil

import pytest

import spikeinterface.extractors as se
import spikeinterface.sorters as ss

os.environ['SINGULARITY_DISABLE_CACHE'] = 'true'

# test docker or singularity
DOCKER_SINGULARITY = "singularity" # "docker"


def generate_run_kwargs(DOCKER_SINGULARITY):
    test_recording, _ = se.toy_example(
        duration=30,
        seed=0,
        num_channels=64,
        num_segments=1
    )
    test_recording = test_recording.save(name='toy')
    run_kwargs = dict(recording=test_recording, verbose=True)
    if DOCKER_SINGULARITY == "singularity":
        run_kwargs["singularity_image"] = True
    elif DOCKER_SINGULARITY == "docker":
        run_kwargs["docker_image"] = True
    else:
        raise Exception("DOCKER_SINGULARITY can be 'docker' or 'singularity'")
    return run_kwargs

@pytest.fixture(autouse=True)
def work_dir(request, tmp_path):
    """
    This fixture, along with "run_kwargs" creates one folder per
    test function using built-in tmp_path pytest fixture

    The tmp_path will be the working directory for the test function

    At the end of the each test function, a clean up will be done
    """
    os.chdir(tmp_path)
    yield
    os.chdir(request.config.invocation_dir)
    shutil.rmtree(str(tmp_path))


@pytest.fixture
def run_kwargs(work_dir):
    return generate_run_kwargs()


def test_kilosort2(run_kwargs):
    sorting = ss.run_kilosort2(output_folder="kilosort2", **run_kwargs)
    print(sorting)


def test_kilosort2_5(run_kwargs):
    sorting = ss.run_kilosort2_5(output_folder="kilosort2_5", **run_kwargs)
    print(sorting)


def test_kilosort3(run_kwargs):
    sorting = ss.run_kilosort3(output_folder="kilosort3", **run_kwargs)
    print(sorting)


def test_yass(run_kwargs):
    sorting = ss.run_yass(output_folder="yass", **run_kwargs)
    print(sorting)


def test_pykilosort(run_kwargs):
    sorting = ss.run_pykilosort(output_folder="pykilosort", **run_kwargs)
    print(sorting)

if __name__ == "__main__":
    kwargs = _run_kwargs()
    test_pykilosort(kwargs)