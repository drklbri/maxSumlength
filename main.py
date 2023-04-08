class Segment:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.length = end - start


def read_segments(input_file):
    sections = []
    for line in input_file:
        x1, x2 = line.split()
        sections.append(Segment(int(x1), int(x2)))
    input_file.close()
    return sections


def write_segments(list_of_segments, output_file):
    sum_of_segments = sum(segment_length(x) for x in list_of_segments)
    for segment in range(len(list_of_segments)):
        output_file.write(str(list_of_segments[segment].start) + " " + str(list_of_segments[segment].end) + "\n")
    output_file.write("The sum of the lengths of the segments is: " + str(sum_of_segments))
    output_file.close()


def is_intersecting(s1, s2):
    return (s1.start <= s2.start <= s1.end <= s2.end) or (s2.start <= s1.start <= s2.end <= s1.end) or \
           (s1.start <= s2.start <= s2.end <= s1.end) or (s2.start <= s1.start <= s1.end <= s2.end)


def segment_length(segment):
    return segment.end - segment.start


def find_max_sum_segments(list_of_segments):
    max_sum = 0
    max_segments = None
    n = len(list_of_segments)
    for i in range(n):
        for j in range(i + 1, n):
            if is_intersecting(list_of_segments[i], list_of_segments[j]):
                continue
            for k in range(j + 1, n):
                if is_intersecting(list_of_segments[i], list_of_segments[k]) or is_intersecting(list_of_segments[j],
                                                                                                list_of_segments[k]):
                    continue
                sum_lengths = segment_length(list_of_segments[i]) + segment_length(list_of_segments[j]) \
                                                                  + segment_length(list_of_segments[k])
                if sum_lengths > max_sum:
                    max_sum = sum_lengths
                    max_segments = (list_of_segments[i], list_of_segments[j], list_of_segments[k])
    return max_segments


i_file = open("input.txt", "r")
o_file = open("output.txt", "w")

write_segments(find_max_sum_segments(read_segments(i_file)), o_file)
