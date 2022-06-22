import os
import shutil

import pytest

import spikeinterface.extractors as se
import spikeinterface.sorters as ss


@pytest.fixture
def work_dir(request, tmpdir_factory):
    tmpdir = tmpdir_factory.mktemp("work_dir")
    os.chdir(tmpdir)
    yield
    os.chdir(request.config.invocation_dir)
    shutil.rmtree(str(tmpdir))


@pytest.fixture
def run_kwargs(work_dir):
    test_recording, _ = se.toy_example(
        duration=30,
        seed=0,
        num_channels=64,
        num_segments=1
    )
    test_recording = test_recording.save(name='toy')
    return dict(recording=test_recording, verbose=True, singularity_image=True)


def test_spykingcircus(run_kwargs):
    sorting = ss.run_spykingcircus(output_folder="spykingcircus", **run_kwargs)
    print(sorting)


def test_mountainsort4(run_kwargs):
    sorting = ss.run_mountainsort4(output_folder="mountainsort4", **run_kwargs)
    print(sorting)


def test_tridesclous(run_kwargs):
    sorting = ss.run_tridesclous(output_folder="tridesclous", **run_kwargs)
    print(sorting)


def test_klusta(run_kwargs):
    sorting = ss.run_klusta(output_folder="klusta", **run_kwargs)
    print(sorting)


def test_ironclust(run_kwargs):
    sorting = ss.run_ironclust(output_folder="ironclust", fGpu=False, **run_kwargs)
    print(sorting)


def test_waveclus(run_kwargs):
    sorting = ss.run_waveclus(output_folder="waveclus", **run_kwargs)
    print(sorting)


def test_hdsort(run_kwargs):
    sorting = ss.run_hdsort(output_folder="hdsort", **run_kwargs)
    print(sorting)


@pytest.mark.skip(reason='Image for KiloSort 1 not implemented yet')
def test_kilosort1(run_kwargs):
    sorting = ss.run_kilosort(output_folder="kilosort", useGPU=False, **run_kwargs)
    print(sorting)


@pytest.mark.skip(reason="GPU required")
def test_kilosort2(run_kwargs):
    sorting = ss.run_kilosort2(output_folder="kilosort2", **run_kwargs)
    print(sorting)


@pytest.mark.skip(reason="GPU required")
def test_kilosort2_5(run_kwargs):
    sorting = ss.run_kilosort2_5(output_folder="kilosort2_5", **run_kwargs)
    print(sorting)


@pytest.mark.skip(reason="GPU required")
def test_kilosort3(run_kwargs):
    sorting = ss.run_kilosort3(output_folder="kilosort3", **run_kwargs)
    print(sorting)


@pytest.mark.skip(reason="GPU required")
def test_pykilosort(run_kwargs):
    sorting = ss.run_pykilosort(output_folder="pykilosort", **run_kwargs)
    print(sorting)
