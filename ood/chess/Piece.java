public abstract class Piece {
    private boolean isDead = false;
    private boolean isWhite = false;

    public Piece(boolean isWhite) {
        this.setWhite(isWhite);
    }

    public boolean isWhite() {
        return this.isWhite;
    }

    public void setWhite(boolean isWhite) {
        this.isWhite = isWhite;
    }

    public boolean isDead() {
        return this.isDead;
    }

    public void setDead(boolean killed) {
        this.isDead = killed;
    }

    public abstract boolean canMove(Board board, Spot start, Spot end);

    public boolean isCastlingMove(Spot start, Spot end) {
        return false;
    }
}
