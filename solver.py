#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from subprocess import Popen, PIPE


def solve_it(input_data):

    # Writes the inputData to a temporay file

    tmp_file_name = 'tmp.data'
    tmp_file = open(tmp_file_name, 'w')
    tmp_file.write(input_data)
    tmp_file.close()

    # Runs the command: java Solver -file=tmp.data

    classpath = "C:/Program Files/Java/jdk1.8/jre/lib/charsets.jar;C:/Program Files/Java/jdk1.8/jre/lib/deploy.jar;C:/Program Files/Java/jdk1.8/jre/lib/ext/access-bridge-64.jar;C:/Program Files/Java/jdk1.8/jre/lib/ext/cldrdata.jar;C:/Program Files/Java/jdk1.8/jre/lib/ext/dnsns.jar;C:/Program Files/Java/jdk1.8/jre/lib/ext/jaccess.jar;C:/Program Files/Java/jdk1.8/jre/lib/ext/jfxrt.jar;C:/Program Files/Java/jdk1.8/jre/lib/ext/localedata.jar;C:/Program Files/Java/jdk1.8/jre/lib/ext/nashorn.jar;C:/Program Files/Java/jdk1.8/jre/lib/ext/sunec.jar;C:/Program Files/Java/jdk1.8/jre/lib/ext/sunjce_provider.jar;C:/Program Files/Java/jdk1.8/jre/lib/ext/sunmscapi.jar;C:/Program Files/Java/jdk1.8/jre/lib/ext/sunpkcs11.jar;C:/Program Files/Java/jdk1.8/jre/lib/ext/zipfs.jar;C:/Program Files/Java/jdk1.8/jre/lib/javaws.jar;C:/Program Files/Java/jdk1.8/jre/lib/jce.jar;C:/Program Files/Java/jdk1.8/jre/lib/jfr.jar;C:/Program Files/Java/jdk1.8/jre/lib/jfxswt.jar;C:/Program Files/Java/jdk1.8/jre/lib/jsse.jar;C:/Program Files/Java/jdk1.8/jre/lib/management-agent.jar;C:/Program Files/Java/jdk1.8/jre/lib/plugin.jar;C:/Program Files/Java/jdk1.8/jre/lib/resources.jar;C:/Program Files/Java/jdk1.8/jre/lib/rt.jar;C:/Users/Tibi/src/discrete-optim/coloring/out/production/classes;C:/Users/ycht/.gradle/caches/modules-2/files-2.1/org.jetbrains.kotlin/kotlin-stdlib-jdk8/1.2.30/f916048adc012c9342b796a5f84c0ac6205abcac/kotlin-stdlib-jdk8-1.2.30.jar;C:/Users/ycht/.gradle/caches/modules-2/files-2.1/org.choco-solver/choco-solver/4.0.6/34095412f9f9e747779e08490957ae2b070dc9a7/choco-solver-4.0.6.jar;C:/Users/ycht/.gradle/caches/modules-2/files-2.1/org.jetbrains.kotlin/kotlin-stdlib-jdk7/1.2.30/ca12c47fc1e3a7316067b2a51e2f214745ebf8c5/kotlin-stdlib-jdk7-1.2.30.jar;C:/Users/ycht/.gradle/caches/modules-2/files-2.1/org.jetbrains.kotlin/kotlin-stdlib/1.2.30/2dfac33f8b4e92c9dd1422cd286834701a6f6d6/kotlin-stdlib-1.2.30.jar;C:/Users/ycht/.gradle/caches/modules-2/files-2.1/org.choco-solver/choco-sat/1.0.2/4fe93b568dac6f945e83612aa3449c9419e350ed/choco-sat-1.0.2.jar;C:/Users/ycht/.gradle/caches/modules-2/files-2.1/org.choco-solver/cutoffseq/1.0.2/1028bd2e8e73e3b64a344cf3be1b9906366c1068/cutoffseq-1.0.2.jar;C:/Users/ycht/.gradle/caches/modules-2/files-2.1/net.sf.trove4j/trove4j/3.0.3/42ccaf4761f0dfdfa805c9e340d99a755907e2dd/trove4j-3.0.3.jar;C:/Users/ycht/.gradle/caches/modules-2/files-2.1/dk.brics.automaton/automaton/1.11-8/6ebfa65eb431ff4b715a23be7a750cbc4cc96d0f/automaton-1.11-8.jar;C:/Users/ycht/.gradle/caches/modules-2/files-2.1/org.jgrapht/jgrapht-core/1.1.0/b0b4357e6eea77945ca1c1920f865e0cfbbd67f2/jgrapht-core-1.1.0.jar;C:/Users/ycht/.gradle/caches/modules-2/files-2.1/com.github.cp-profiler/cpprof-java/1.3.0/42f77bab064bf05e37bc8d87b10c95f02ce69636/cpprof-java-1.3.0.jar;C:/Users/ycht/.gradle/caches/modules-2/files-2.1/org.jetbrains/annotations/13.0/919f0dfe192fb4e063e7dacadee7f8bb9a2672a9/annotations-13.0.jar;C:/Users/ycht/.gradle/caches/modules-2/files-2.1/com.google.protobuf/protobuf-java/2.6.1/d9521f2aecb909835746b7a5facf612af5e890e8/protobuf-java-2.6.1.jar"
    process = Popen('java -classpath "' + classpath + '" MainKt -file=' + tmp_file_name, stdout=PIPE)
    (stdout, stderr) = process.communicate()

    # removes the temporay file
    os.remove(tmp_file_name)

    return stdout.strip().decode("utf-8")


import sys

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)')

