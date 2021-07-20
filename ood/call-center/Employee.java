public class Employee {
    private Call currentCall = null;
    protected Rank rank;
    private final CallHandler callHandler;

    public Employee(CallHandler handler) {
        callHandler = handler;
    }

    /* Take the call */
    public void receiveCall(Call call) {
        currentCall = call;
    }

    /* Return true if employee is free to take call */
    public boolean isFree() {
        return currentCall == null;
    }

    /* Return the rank of employee */
    public Rank getRank() {
        return rank;
    }

    /* Finish the call */
    public void callCompleted() {
        if (currentCall != null) {
            currentCall.disconnect();
            currentCall = null;
        }

        /* Check if the employee is able to take new call */
        assignNewCall();
    }

    /* Assign new call to an employee */
    public boolean assignNewCall() {
        if (!isFree()) {
            return false;
        }
        return callHandler.assignCall(this);
    }

    /* The issue is not resolved. Escalate the call and assign a new call */
    public void escalateAndReassign() {
        if (currentCall != null) {
            if (currentCall.getRank() == Rank.Director) {
                currentCall.reply("The call cannot be escalated. Please hang up");
                currentCall.disconnect();
            }
            currentCall.reply("The call is going to be escalated");
            currentCall.incrementRank();
            callHandler.dispatchCall(currentCall);

            /* free the employee */
            assignNewCall();
        }
    }
}
