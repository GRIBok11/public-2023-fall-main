import typing as tp
import heapq

def merge(input_streams: tp.Sequence[tp.IO[bytes]], output_stream: tp.IO[bytes]) -> None:
    """
    Merge input_streams in output_stream
    :param input_streams: list of input streams. Contains byte-strings separated by "\n". Nonempty stream ends with "\n"
    :param output_stream: output stream. Contains byte-strings separated by "\n". Nonempty stream ends with "\n"
    :return: None
    """
    heap = []
    for stream_index, stream in enumerate(input_streams):
        line = stream.readline()
        if line:
            heapq.heappush(heap, (line, stream_index))

    while heap:
        smallest, stream_index = heapq.heappop(heap)
        output_stream.write(smallest)
        next_line = input_streams[stream_index].readline()
        if next_line:
            heapq.heappush(heap, (next_line, stream_index))