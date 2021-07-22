public class Edge {
    private Shape shape;
    private String code;
    private Piece parentPiece;

    public Edge(Shape shape, String code) {
        this.shape = shape;
        this.code = code;
    }

    public Shape getShape() {
        return shape;
    }

    private String getCode() {
        return code;
    }

    public void setParentPiece(Piece piece) {
        this.parentPiece = piece;
    }

    public Piece getParentPiece() {
        return parentPiece;
    }

    /* Create an edge that can fit the edge */
    public Edge _createMatchingEdge() {
        if (shape == Shape.FLAT) return null;
        return new Edge(shape.getOpposite(), getCode());
    }

    /* Check if the edge fits into the other edge */
    public boolean fitsWith(Edge edge) {
        return edge.getCode().equals(this.getCode());
    }

    public String toString() {
        return code;
    }

}
