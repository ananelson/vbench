## "imports"
from vbench.api import Benchmark
from vbench.api import BenchmarkRunner

### "benchmark"
setup_code = "import datetime"
benchmark_code = "print 'hello'"
benchmark = Benchmark(benchmark_code, setup_code)

### "runner"
benchmarks = [benchmark]
runner = BenchmarkRunner(
        benchmarks, # list of benchmarks
        ".", # repo path
        "git://github.com/pydata/vbench.git", # repo url
        "", # build cmd
        "benchmarks.db", # db file
        "/tmp", # temp dir - TODO why not use python tempdir?
        "", # prep cmd
        use_blacklise = True)

runner.run()
