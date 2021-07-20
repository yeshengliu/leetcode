/*
 * Represents a call from user. Call is assigned to the first
 * available employee
 */

public class Call {
    /* Minimal rank of employee who can handle this call */
    private Rank rank;

    /* Person who is calling */
    private Caller caller;

    /* Employee who is handling the call */
    private Employee handler;

    public Call(Caller c) {
        rank = Rank.Responder;
        caller = c;
    }

    /* Set employee who is handling the call */
    public void setHandler(Employee e) {
        handler = e;
    }

    /* Play recorded message to customer */
    public void reply(String message) {
        System.out.println(message);
    }

    /* Disconnect call */
    public void disconnect() {
        reply("Thank you for calling");
    }

    /* Return rank */
    public Rank getRank() {
        return rank;
    }

    /* Set rank */
    public void setRank(Rank r) {
        rank = r;
    }

    /* Increment rank */
    public Rank incrementRank() {
        if (rank == Rank.Responder) {
            rank = Rank.Manager;
        } else if (rank == Rank.Manager) {
            rank = Rank.Director;
        }
        return rank;
    }
}
