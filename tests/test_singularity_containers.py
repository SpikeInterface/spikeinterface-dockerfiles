import os
import shutil

import pytest

import spikeinterface.sorters as ss
from spikeinterface.core.testing_tools import generate_recording


@pytest.fixture
def work_dir(request, tmpdir_factory):
    tmpdir = tmpdir_factory.mktemp("work_dir")
    os.chdir(tmpdir)
    yield
    os.chdir(request.config.invocation_dir)
    shutil.rmtree(str(tmpdir))


@pytest.fixture
def run_kwargs(work_dir):

    test_recording = generate_recording(
        num_channels=32,
        sampling_frequency=30000.0,  # in Hz
        durations=[120],
        set_probe=True,
        ndim=2,
    )
    test_recording = test_recording.save(folder="test_recording")
    return dict(recording=test_recording, verbose=True, singularity_image=True)


@pytest.mark.xfail(reason="FAILING: investigate why")
def test_spyking_circus(run_kwargs):
    ss.run_spykingcircus(output_folder="spyking_circus", **run_kwargs)


@pytest.mark.xfail(reason="FAILING: investigate why")
def test_mountainsort4(run_kwargs):
    ss.run_mountainsort4(output_folder="mountainsort4", **run_kwargs)


def test_tridesclous(run_kwargs):
    ss.run_tridesclous(output_folder="tridesclous", **run_kwargs)


def test_klusta(run_kwargs):
    ss.run_klusta(output_folder="klusta", **run_kwargs)


def test_ironclust(run_kwargs):
    ss.run_ironclust(output_folder="ironclust", fGpu=False, **run_kwargs)


def test_waveclus(run_kwargs):
    ss.run_waveclus(output_folder="waveclus", **run_kwargs)


def test_hdsort(run_kwargs):
    ss.run_hdsort(output_folder="hdsort", **run_kwargs)


def test_kilosort1(run_kwargs):
    ss.run_kilosort(output_folder="kilosort", useGPU=False, **run_kwargs)


@pytest.mark.skip(reason="GPU required")
def test_kilosort2(run_kwargs):
    ss.run_kilosort2(output_folder="kilosort2", **run_kwargs)


@pytest.mark.skip(reason="GPU required")
def test_kilosort2_5(run_kwargs):
    ss.run_kilosort2_5(output_folder="kilosort2_5", **run_kwargs)


@pytest.mark.skip(reason="GPU required")
def test_kilosort3(run_kwargs):
    ss.run_kilosort3(output_folder="kilosort3", **run_kwargs)


@pytest.mark.skip(reason="GPU required")
def test_pykilosort(run_kwargs):
    ss.run_pykilosort(output_folder="pykilosort", **run_kwargs)
