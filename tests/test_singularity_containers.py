#from spikeinterface.extractors import toy_example
import spikeinterface.sorters as ss
from spikeinterface.core.testing_tools import generate_recording

recording = generate_recording(
    num_channels=32,
    sampling_frequency=30000.,  # in Hz
    durations=[120],  #  in s for 2 segments
    set_probe=True,
    ndim=2,
)
#recording = toy_example(num_segments=1, num_channels=32, duration=120)[0]
recording2 = recording.save(folder="test_recording")
# recording2 = si.load_extractor("test_recording11")


def test_spyking_circus():

    ss.run_spykingcircus(
        recording2,
        output_folder="spyking_circus",
        singularity_image="spikeinterface/spyking-circus-base:1.1.0",
        verbose=True
    )