import sys
import time

### I/O wrapper ###
class FileParser:
    """Read numbers/strings from file (or stdin by default), one line by one.
    """

    def __init__(self, filepath=None, type=None):
        if filepath is None:
            self.fd = sys.stdin
        else:
            self.fd = open(filepath, type)

    def read_string(self):
        return self.fd.readline().rstrip()

    def read_words(self):
        return [x for x in self.read_string().split()]

    def read_int(self):
        return int(self.fd.readline())

    def read_integers(self):
        return [int(x) for x in self.fd.readline().rstrip().split()]

    def read_float(self):
        return float(self.fd.readline())

    def read_floats(self):
        return [float(x) for x in self.fd.readline().rstrip().split()]

    def write(self, context):
        if self.fd is not sys.stdin:
            self.fd.write(context+"\n")
        else:
            print(context)
        return

    def close(self):
        if self.fd is not sys.stdin:
            self.fd.close()
        self.fd = None


### specify the problem meta information ###
problemID = "A" # A, B, C, D...
problemSize = "small" # small, large, local
#filename = "%s-%s-practice" % (problemID, problemSize)
filename = "A-small-attempt0"

### the algorithm that solve the cases ###
def solve(name):
    # record the start timing
    timing.append(time.time())
    leader, count = [], 0
    for n in name:
        character = set()
        for c in n:
            character.add(c)
        if len(character) > count:
            leader = [n]
            count = len(character)
        elif len(character) == count:
            leader.append(n)
    ans = sorted(leader)[0]
    timing.append(time.time())
    return ans

### solve the test cases ###
# for the purpose of counting the total elapsed time
timing = [time.time()]

# open the input / output files
f_in = FileParser(filename+".in", "r")
f_out = FileParser(filename+".out", "w")


# solve each test case
T = f_in.read_int()
for caseID in range(1, T+1):
    # read the input data of each case
    # f_in.read_string(), f_in.read_words()
    # f_in.read_int(), f_in.read_integers()
    # f_in.read_float(), f_in.read_floats()
    N = f_in.read_int()
    name = []
    for _ in range(N):
        name.append(f_in.read_string())

    # solve the case
    ans = solve(name)

    # print the answer to output file
    context = "Case #%d: %s" % (caseID, ans)
    print(context, "\t\t Elapsed: %.2f seconds" % (timing[-1] - timing[-2]))
    f_out.write(context)

# close the input / output files
f_in.close()
f_out.close()

# output the total elapsed time
timing.append(time.time())
total_time = timing[-1] - timing[0]
print("Total elapsed time: %.2f seconds / %.2f minutes" % ((total_time, total_time/60)))
