import java.util.ArrayList;
import java.util.List;

public class CallHandler {
    /* 3 levels of employees: respondents, managers, directors */
    private final int LEVELS = 3;

    /* Initialize with 10 respondents, 4 managers, and 2 directors */
    private final int NUM_RESPONDENTS = 10;
    private final int NUM_MANAGERS = 4;
    private final int NUM_DIRECTORS = 2;

    /* List of employees by level
     * employeeLevels[0] = respondents;
     * employeeLevels[1] = managers;
     * employeeLevels[2] = directors
     */
    List<List<Employee>> employeeLevels;

    /* Call queue by level */
    List<List<Call>> callQueues;

    public CallHandler() {
        employeeLevels = new ArrayList<>(LEVELS);
        callQueues = new ArrayList<>(LEVELS);

        // Respondents
        List<Employee> respondents = new ArrayList<>(NUM_RESPONDENTS);
        for (int k = 0; k < NUM_RESPONDENTS; k++) {
            respondents.add(new Respondent(this));
        }
        employeeLevels.add(respondents);

        // Managers
        List<Employee> managers = new ArrayList<>(NUM_MANAGERS);
        for (int k = 0; k < NUM_MANAGERS; k++) {
            managers.add(new Manager(this));
        }
        employeeLevels.add(managers);

        // Directors
        List<Employee> directors = new ArrayList<>(NUM_DIRECTORS);
        for (int k = 0; k < NUM_DIRECTORS; k++) {
            directors.add(new Director(this));
        }
        employeeLevels.add(directors);
    }

    /* Return the first available employee who can handle the call */
    public Employee getHandlerForCall(Call call) {
        for (int level = call.getRank().getValue(); level < LEVELS; level++) {
            List<Employee> employeeLevel = employeeLevels.get(level);
            for (Employee emp : employeeLevel) {
                if (emp.isFree()) {
                    return emp;
                }
            }
        }
        return null;
    }

    /* Route the call to an available employee or save into a queue
       if no employee available
     */
    public void dispatchCall(Caller caller) {
        Call call = new Call(caller);
        dispatchCall(call);
    }

    public void dispatchCall(Call call) {
        Employee emp = getHandlerForCall(call);
        if (emp != null) {
            emp.receiveCall(call);
            call.setHandler(emp);
        } else {
            call.reply("Call service is busy, please wait for next available employee");
            callQueues.get(call.getRank().getValue()).add(call);
        }
    }

    /* Return true if the new available employee is able to take a call */
    public boolean assignCall(Employee emp) {
        for (int rank = emp.getRank().getValue(); rank >= 0; rank--) {
            List<Call> calls = callQueues.get(rank);

            /* Remove the first call, if any */
            if (calls.size() > 0) {
                Call call = calls.remove(0);
                if (call != null) {
                    emp.receiveCall(call);
                    return true;
                }
            }
        }
        return false;
    }
}
