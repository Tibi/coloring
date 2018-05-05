
import org.chocosolver.solver.Model
import java.io.File


/**
 * Graph coloring assignment, using Choco solver.
 *
 * @author YCHT
 */
fun main(args: Array<String>) {

    val graph = Graph("./data/gc_1000_5")

    val model = Model("Graph Coloring")
    val vars = model.intVarArray("C", graph.numNodes, 0, graph.numNodes, false)
    graph.edges.forEach { vars[it.first].ne(vars[it.second]).post() }
    val solution = model.solver.findSolution()
    val max = vars.map { solution.getIntVal(it) }.max()
    println("${max!! + 1} colors")
    println(solution)
}

class Graph(fileName: String) {
    var numNodes = 0
    val edges = readFile(fileName)

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