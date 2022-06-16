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

# python-based
@pytest.mark.xfail(reason="FAILING: investigate why")
def test_spyking_circus():

    ss.run_spykingcircus(
        recording2, output_folder="spyking_circus", singularity_image=True, verbose=True
    )


def test_tridescluos():

    ss.run_tridesclous(
        recording2, output_folder="tridesclous", singularity_image=True, verbose=True
    )


def test_klusta():

    ss.run_klusta(
        recording2, output_folder="klusta", singularity_image=True, verbose=True
    )


@pytest.mark.xfail(reason="FAILING: investigate why")
def test_mountainsort4():

    ss.run_mountainsort4(
        recording2, output_folder="mountainsort4", singularity_image=True, verbose=True
    )


# matlab-based
def test_ironclust():

    ss.run_ironclust(
        recording2,
        output_folder="ironclust",
        singularity_image=True,
        fGpu=False,
        verbose=True,
    )


def test_waveclus():

    ss.run_waveclus(
        recording2, output_folder="waveclus", singularity_image=True, verbose=True
    )


def test_hdsort():

    ss.run_hdsort(
        recording2, output_folder="hdsort", singularity_image=True, verbose=True
    )


def test_kilosort1():

    ss.run_kilosort(
        recording2,
        output_folder="kilosort",
        singularity_image=True,
        useGPU=False,
        verbose=True,
    )


# gpu-required
@pytest.mark.skip(reason="GPU required")
def test_kilosort2():

    ss.run_kilosort2(
        recording2, output_folder="kilosort2", singularity_image=True, verbose=True
    )


@pytest.mark.skip(reason="GPU required")
def test_kilosort2_5():

    ss.run_kilosort2_5(
        recording2, output_folder="kilosort2_5", singularity_image=True, verbose=True
    )


@pytest.mark.skip(reason="GPU required")
def test_kilosort3():

    ss.run_kilosort3(
        recording2, output_folder="kilosort3", singularity_image=True, verbose=True
    )


@pytest.mark.skip(reason="GPU required")
def test_pykilosort():

    ss.run_pykilosort(
        recording2, output_folder="pykilosort", singularity_image=True, verbose=True
    )
