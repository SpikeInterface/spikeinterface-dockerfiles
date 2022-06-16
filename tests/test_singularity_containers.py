import pytest

import spikeinterface.sorters as ss
from spikeinterface.core.testing_tools import generate_recording

recording = generate_recording(
    num_channels=32,
    sampling_frequency=30000.0,  # in Hz
    durations=[120],
    set_probe=True,
    ndim=2,
)

recording2 = recording.save(folder="test_recording")

kwargs = dict(recordin=recording2, verbose=True, singularity_image=True)


@pytest.mark.xfail(reason="FAILING: investigate why")
def test_spyking_circus():
    ss.run_spykingcircus(output_folder="spyking_circus", **kwargs)


@pytest.mark.xfail(reason="FAILING: investigate why")
def test_mountainsort4():
    ss.run_mountainsort4(output_folder="mountainsort4", **kwargs)


def test_tridesclous():
    ss.run_tridesclous(output_folder="tridesclous", **kwargs)


def test_klusta():
    ss.run_klusta(output_folder="klusta", **kwargs)


def test_ironclust():
    ss.run_ironclust(output_folder="ironclust", fGpu=False, **kwargs)


def test_waveclus():
    ss.run_waveclus(output_folder="waveclus", **kwargs)


def test_hdsort():
    ss.run_hdsort(output_folder="hdsort", **kwargs)


def test_kilosort1():
    ss.run_kilosort(output_folder="kilosort", useGPU=False, **kwargs)


@pytest.mark.skip(reason="GPU required")
def test_kilosort2():
    ss.run_kilosort2(output_folder="kilosort2", **kwargs)


@pytest.mark.skip(reason="GPU required")
def test_kilosort2_5():
    ss.run_kilosort2_5(output_folder="kilosort2_5", **kwargs)


@pytest.mark.skip(reason="GPU required")
def test_kilosort3():
    ss.run_kilosort3(output_folder="kilosort3", **kwargs)


@pytest.mark.skip(reason="GPU required")
def test_pykilosort():
    ss.run_pykilosort(output_folder="pykilosort", **kwargs)
