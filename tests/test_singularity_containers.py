import pytest

import spikeinterface.sorters as ss
from spikeinterface.core.testing_tools import generate_recording

recording = generate_recording(
    num_channels=32,
    sampling_frequency=30000.,  # in Hz
    durations=[120],
    set_probe=True,
    ndim=2,
)

recording2 = recording.save(folder="test_recording")

# python-based
@pytest.mark.skip(reason="FAILING: investigate why")
def test_spyking_circus():

    ss.run_spykingcircus(
        recording2,
        output_folder="spyking_circus",
        singularity_image="spikeinterface/spyking-circus-base:1.1.0",
        verbose=True
    )


def test_tridescluos():

    ss.run_tridesclous(
        recording2,
        output_folder="tridesclous",
        singularity_image="spikeinterface/tridesclous-base:1.6.5",
        verbose=True
    )

def test_klusta():

    ss.run_klusta(
        recording2,
        output_folder="klusta",
        singularity_image="spikeinterface/klusta-base:0.2.7",
        verbose=True
    )

@pytest.mark.skip(reason="FAILING: investigate why")
def test_mountainsort4():

    ss.run_mountainsort4(
        recording2,
        output_folder="mountainsort4",
        singularity_image="spikeinterface/mountainsort4-base:1.0.0",
        verbose=True
    )

# matlab-based
def test_ironclust():

    ss.run_ironclust(
        recording2,
        output_folder="ironclust",
        singularity_image="spikeinterface/ironclust-compiled-base:5.9.8",
        fGpu=False,
        verbose=True
    )
    

def test_waveclus():

    ss.run_waveclus(
        recording2,
        output_folder="waveclus",
        singularity_image="spikeinterface/waveclus-compiled-base:0.1.0",
        verbose=True
    )


def test_hdsort():

    ss.run_hdsort(
        recording2,
        output_folder="hdsort",
        singularity_image="spikeinterface/hdsort-compiled-base:0.1.0",
        verbose=True
    )
    
    
def test_kilosort1():

    ss.run_kilosort(
        recording2,
        output_folder="kilosort",
        singularity_image="spikeinterface/kilosort-compiled-base:0.1.0",
        useGPU=False,
        verbose=True
    )
    

# gpu-required
@pytest.mark.skip(reason="GPU required")
def test_kilosort2():

    ss.run_kilosort2(
        recording2,
        output_folder="kilosort2",
        singularity_image="spikeinterface/kilosort2-compiled-base:0.1.0",
        verbose=True
    )

@pytest.mark.skip(reason="GPU required")
def test_kilosort2_5():

    ss.run_kilosort2_5(
        recording2,
        output_folder="kilosort2_5",
        singularity_image="spikeinterface/kilosort2_5-compiled-base:0.1.0",
        verbose=True
    )

@pytest.mark.skip(reason="GPU required")
def test_kilosort3():

    ss.run_kilosort3(
        recording2,
        output_folder="kilosort3",
        singularity_image="spikeinterface/kilosort3-compiled-base:0.1.0",
        verbose=True
    )

@pytest.mark.skip(reason="GPU required")  
def test_pykilosort():

    ss.run_pykilosort(
        recording2,
        output_folder="pykilosort",
        singularity_image="spikeinterface/pykilosort-base:0.1.0",
        verbose=True
    )