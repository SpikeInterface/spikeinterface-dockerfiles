import os
import shutil

import pytest

import spikeinterface.sorters as ss
from spikeinterface.core.testing_tools import generate_recording


@pytest.fixture
def work_dir(request, tmpdir_factory):
    tmpdir = tmpdir_factory.mktemp('work_dir')
    os.chdir(tmpdir)
    yield
    os.chdir(request.config.invocation_dir)
    shutil.rmtree(str(tmpdir))


@pytest.fixture
def recording(work_dir):

    test_recording = generate_recording(
        num_channels=32,
        sampling_frequency=30000.0,  # in Hz
        durations=[120],
        set_probe=True,
        ndim=2,
    )
    test_recording = test_recording.save(folder="test_recording")
    return test_recording


def test_spyking_circus(recording, work_dir):

    ss.run_spykingcircus(
        recording,
        output_folder="spyking_circus",
        singularity_image="spikeinterface/spyking-circus-base:1.1.0",
        verbose=True
    )


def test_tridecluos(recording):

    ss.run_tridesclous(
        recording,
        output_folder="tridesclous",
        singularity_image="spikeinterface/tridesclous-base:1.6.5",
        verbose=True
    )


def test_ironclust(recording):

    ss.run_ironclust(
        recording,
        output_folder="ironclust",
        singularity_image="spikeinterface/ironclust-compiled-base:5.9.8",
        verbose=True
    )
