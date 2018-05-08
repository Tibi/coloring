
import org.chocosolver.solver.Model
import org.chocosolver.solver.search.loop.monitors.IMonitorSolution
import org.chocosolver.solver.search.strategy.Search
import org.chocosolver.solver.search.strategy.selectors.values.IntDomainBest
import org.chocosolver.solver.search.strategy.selectors.values.IntValueSelector
import org.chocosolver.solver.search.strategy.selectors.variables.VariableSelector
import org.chocosolver.solver.variables.IntVar
import java.io.File


/**
 * Graph coloring assignment, using Choco solver.
 *
 * @author YCHT
 */
fun main(args: Array<String>) {

//    val graph = Graph("./data/gc_20_1")
    val graph = Graph("./data/gc_1000_5")

    val model = Model("Graph Coloring")
    // One int color variable for each node
    val nodes = model.intVarArray("C", graph.numNodes, 0, graph.numNodes, false)
    // A != constraint for each edge
    graph.edges.forEach { nodes[it.first].ne(nodes[it.second]).post() }

    // The maximum color used, for the objective
    val maxCol = model.intVar("maxCol", 1, 800)
    model.max(maxCol, nodes).post()

    // Search strategy: high degree nodes first
    val degrees = mutableMapOf<IntVar, Int>()
    for (i in 0 until nodes.size) {
        degrees[nodes[i]] = graph.nodeDegrees[i]
    }
    val varSel = VariableSelector<IntVar> { vars:Array<IntVar> ->
        val bestVar = vars.filter { !it.isInstantiated() }
            .sortedWith(compareBy({ it.domainSize }, { -(degrees[it] ?: 0) })).firstOrNull()
//        println("selecting ${bestVar} of degree ${degrees[bestVar]}")
        bestVar
    }
    val valSel = IntValueSelector { it.lb }
    model.solver.setSearch(Search.intVarSearch(varSel, IntDomainBest(), *nodes))

    model.solver.plugMonitor(IMonitorSolution { println("${maxCol.value + 1} colors") })

    model.solver.findOptimalSolution(maxCol, false)
}


class Graph(fileName: String) {
    var numNodes = 0
    val edges = readFile(fileName)
    val nodeDegrees = IntArray(numNodes) { i -> edges.count { it.first == i || it.second == i } }

    fun readFile(name: String): Array<Pair<Int, Int>> {
        val lines = File(name).readLines()
        val firstLine = lines[0].split(" ")
        numNodes = firstLine[0].toInt()
        val numEdges = firstLine[1].toInt()
        return Array(numEdges) {
            val line = lines[it + 1].split(" ")
            Pair(line[0].toInt(), line[1].toInt())
        }
    }
}