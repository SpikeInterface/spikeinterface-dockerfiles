from spikeinterface.extractors import toy_example
import spikeinterface.sorters as ss

recording = toy_example(num_segments=1, num_channels=32, duration=120)[0]
recording2 = recording.save("test_recording")
# recording2 = si.load_extractor("test_recording11")


def test_spyking_circus():

    ss.run_spykingcircus(
        recording2,
        output_folder="spyking_circus",
        singularity_image="spikeinterface/spyking-circus-base:1.1.0",
        verbose=True
    )