public class Board {
    Spot[][] spots;
    int SIZE_OF_BOARD = 8;

    public Board() {
        this.resetBoard();
    }

    public Spot getSpot(int x, int y) {
        if (x < 0 || x > SIZE_OF_BOARD - 1) {
            throw new IllegalArgumentException("Index x out of bound");
        }
        if (y < 0 || y > SIZE_OF_BOARD - 1) {
            throw new IllegalArgumentException("Index y out of bound");
        }

        return spots[x][y];
    }

    public void resetBoard() {
        /* initialize white pieces */
        /* initialize black pieces */
        /* initialize remaining spots */
        for (int i = 2; i < SIZE_OF_BOARD - 2; i++) {
            for (int j = 0; j < SIZE_OF_BOARD; j++) {
                spots[i][j] = new Spot(i, j, null);
            }
        }
    }
}
