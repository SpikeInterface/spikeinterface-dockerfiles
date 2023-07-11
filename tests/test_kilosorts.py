import os
import shutil
from pathlib import Path

import pytest

import spikeinterface as si
import spikeinterface.extractors as se
import spikeinterface.preprocessing as spre
import spikeinterface.sorters as ss


si_path = Path(si.__file__)

if "site-package" not in si_path.name:
    print("Using SPIKEINTERFACE_DEV_PATH")
    SI_DEV_PATH = str(si_path.parent.parent.parent)
else:
    SI_DEV_PATH = None

os.environ["SINGULARITY_DISABLE_CACHE"] = "true"

# test docker or singularity
DOCKER_SINGULARITY = "docker"  # "singularity" | "docker"


def generate_run_kwargs():
    test_recording, _ = se.toy_example(duration=30, seed=0, num_channels=64, num_segments=1)
    cache_folder = Path("cached_recording")
    if cache_folder.is_dir():
        shutil.rmtree(cache_folder)
    test_recording = test_recording.save(folder="cached_recording")
    test_recording.set_channel_gains(1)
    test_recording.set_channel_offsets(0)
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


def test_kilosort(run_kwargs):
    import os

    os.environ["SPIKEINTERFACE_DEV_PATH"] = SI_DEV_PATH
    sorting = ss.run_sorter("kilosort", output_folder="kilosort", **run_kwargs)
    print(sorting)


def test_kilosort2(run_kwargs):
    import os

    os.environ["SPIKEINTERFACE_DEV_PATH"] = SI_DEV_PATH
    sorting = ss.run_sorter("kilosort2", output_folder="kilosort2", **run_kwargs)
    print(sorting)


def test_kilosort2_release_si(run_kwargs):
    # docker image
    if DOCKER_SINGULARITY == "docker":
        run_kwargs["docker_image"] = "spikeinterface/kilosort2_5-compiled-base:0.2.0"
    else:
        run_kwargs["singularity_image"] = "spikeinterface/kilosort2_5-compiled-base:0.2.0"
    import os

    del os.environ["SPIKEINTERFACE_DEV_PATH"]
    sorting = ss.run_sorter("kilosort2", output_folder="kilosort2", **run_kwargs)
    print(sorting)


def test_kilosort2_5(run_kwargs):
    import os

    os.environ["SPIKEINTERFACE_DEV_PATH"] = SI_DEV_PATH
    sorting = ss.run_sorter("kilosort2_5", output_folder="kilosort2_5", **run_kwargs)
    print(sorting)


def test_kilosort3(run_kwargs):
    import os

    os.environ["SPIKEINTERFACE_DEV_PATH"] = SI_DEV_PATH
    sorting = ss.run_sorter("kilosort3", output_folder="kilosort3", **run_kwargs)
    print(sorting)


def test_kilosort2_skip_preproc(run_kwargs):
    import os

    os.environ["SPIKEINTERFACE_DEV_PATH"] = SI_DEV_PATH
    print("Skipping preprocessing")
    gain = 200
    run_kwargs["recording"] = spre.zscore(run_kwargs["recording"])
    run_kwargs["recording"] = spre.scale(run_kwargs["recording"], gain=gain, dtype="int16")

    sorting = ss.run_sorter(
        "kilosort2", output_folder="kilosort2_skip", skip_kilosort_preprocessing=True, scaleproc=gain, **run_kwargs
    )
    print(sorting)


def test_kilosort2_5_skip_preproc(run_kwargs):
    import os

    os.environ["SPIKEINTERFACE_DEV_PATH"] = SI_DEV_PATH
    print("Skipping preprocessing")
    gain = 200
    run_kwargs["recording"] = spre.zscore(run_kwargs["recording"])
    run_kwargs["recording"] = spre.scale(run_kwargs["recording"], gain=gain, dtype="int16")
    sorting = ss.run_sorter(
        "kilosort2_5", output_folder="kilosort2_5_skip", skip_kilosort_preprocessing=True, scaleproc=gain, **run_kwargs
    )
    print(sorting)


def test_kilosort2_5_old_image(run_kwargs):
    import os

    os.environ["SPIKEINTERFACE_DEV_PATH"] = SI_DEV_PATH

    # docker image
    if DOCKER_SINGULARITY == "docker":
        run_kwargs["docker_image"] = "spikeinterface/kilosort2_5-compiled-base:0.1.0"
    else:
        run_kwargs["singularity_image"] = "spikeinterface/kilosort2_5-compiled-base:0.1.0"
    sorting = ss.run_sorter("kilosort2_5", output_folder="kilosort2_5_old", **run_kwargs)
    print(sorting)


def test_kilosort2_5_skip_preproc_old_image(run_kwargs):
    import os

    os.environ["SPIKEINTERFACE_DEV_PATH"] = SI_DEV_PATH
    print("Skipping preprocessing")
    gain = 200
    run_kwargs["recording"] = spre.zscore(run_kwargs["recording"])
    run_kwargs["recording"] = spre.scale(run_kwargs["recording"], gain=gain, dtype="int16")

    # docker image
    if DOCKER_SINGULARITY == "docker":
        run_kwargs["docker_image"] = "spikeinterface/kilosort2_5-compiled-base:0.1.0"
    else:
        run_kwargs["singularity_image"] = "spikeinterface/kilosort2_5-compiled-base:0.1.0"
    sorting = ss.run_sorter(
        "kilosort2_5",
        output_folder="kilosort2_5_old_skip",
        skip_kilosort_preprocessing=True,
        scaleproc=gain,
        **run_kwargs
    )
    print(sorting)


def test_kilosort3_skip_preproc(run_kwargs):
    import os

    os.environ["SPIKEINTERFACE_DEV_PATH"] = SI_DEV_PATH
    print("Skipping preprocessing")
    run_kwargs["recording"] = spre.zscore(run_kwargs["recording"])
    run_kwargs["recording"] = spre.scale(run_kwargs["recording"], gain=200, dtype="int16")
    sorting = ss.run_sorter(
        "kilosort3", output_folder="kilosort3_skip", skip_kilosort_preprocessing=True, scaleproc=200, **run_kwargs
    )
    print(sorting)


if __name__ == "__main__":
    kwargs = generate_run_kwargs()
    print("\n\nKilosort")
    test_kilosort(kwargs)

    print("\n\nKilosort2")
    test_kilosort2(kwargs)
    test_kilosort2_skip_preproc(kwargs)
    print("\nKilosort2 released si")
    test_kilosort2_release_si(kwargs)

    print("\n\nKilosort2.5")
    test_kilosort2_5(kwargs)
    test_kilosort2_5_skip_preproc(kwargs)
    print("\nKilosort2.5 old image")
    # test_kilosort2_5_old_image(kwargs)

    # This is the only failing test
    # print("\nKilosort2.5 old image - skip")
    # test_kilosort2_5_skip_preproc_old_image(kwargs)

    print("\n\nKilosort3")
    test_kilosort3(kwargs)
    test_kilosort3_skip_preproc(kwargs)
