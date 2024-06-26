import os
import shutil

import pytest

import spikeinterface.extractors as se
import spikeinterface.sorters as ss

os.environ['SINGULARITY_DISABLE_CACHE'] = 'true'

# test docker or singularity
DOCKER_SINGULARITY = "singularity" # "docker"

def clean_singularity_cache():
    print("Cleaning singularity cache")
    os.system("singularity cache clean --force")


def generate_run_kwargs():
    test_recording, _ = se.toy_example(
        duration=30,
        seed=0,
        num_channels=64,
        num_segments=1
    )
    test_recording = test_recording.save(name='toy')
    test_recording.set_channel_gains(1)
    test_recording.set_channel_offsets(1)
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


def test_spykingcircus(run_kwargs):
    if DOCKER_SINGULARITY == "singularity":
        clean_singularity_cache()
    sorting = ss.run_sorter("spykingcircus", folder="spykingcircus", **run_kwargs)
    print(sorting)


def test_mountainsort4(run_kwargs):
    if DOCKER_SINGULARITY == "singularity":
        clean_singularity_cache()
    sorting = ss.run_sorter("mountainsort4", folder="mountainsort4", **run_kwargs)
    print(sorting)


def test_tridesclous(run_kwargs):
    if DOCKER_SINGULARITY == "singularity":
        clean_singularity_cache()
    sorting = ss.run_sorter("tridesclous", folder="tridesclous", **run_kwargs)
    print(sorting)


def test_ironclust(run_kwargs):
    if DOCKER_SINGULARITY == "singularity":
        clean_singularity_cache()
    sorting = ss.run_sorter("ironclust", folder="ironclust", fGpu=False, **run_kwargs)
    print(sorting)


def test_waveclus(run_kwargs):
    if DOCKER_SINGULARITY == "singularity":
        clean_singularity_cache()
    sorting = ss.run_sorter("waveclus", folder="waveclus", **run_kwargs)
    print(sorting)


def test_hdsort(run_kwargs):
    if DOCKER_SINGULARITY == "singularity":
        clean_singularity_cache()
    sorting = ss.run_sorter("hdsort", folder="hdsort", **run_kwargs)
    print(sorting)


def test_kilosort1(run_kwargs):
    if DOCKER_SINGULARITY == "singularity":
        clean_singularity_cache()
    sorting = ss.run_sorter("kilosort", folder="kilosort", useGPU=False, **run_kwargs)
    print(sorting)

def test_combinato(run_kwargs):
    if DOCKER_SINGULARITY == "singularity":
        clean_singularity_cache()
    rec = run_kwargs['recording']
    channels = rec.get_channel_ids()[0:1]
    rec_one_channel = rec.channel_slice(channels)
    run_kwargs['recording'] = rec_one_channel
    sorting = ss.run_sorter("combinato", folder='combinato', **run_kwargs)
    print(sorting)

@pytest.mark.skip(reason="Legcay sorter: requires Python=3.7")
def test_klusta(run_kwargs):
    if DOCKER_SINGULARITY == "singularity":
        clean_singularity_cache()
    recording = run_kwargs["recording"]
    recording.extra_requirements.append("pandas")
    run_kwargs["recording"] = recording
    sorting = ss.run_sorter("klusta", folder="klusta", **run_kwargs)
    print(sorting)

if __name__ == "__main__":
    kwargs = generate_run_kwargs()
    test_ironclust(kwargs)
