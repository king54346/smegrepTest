class Bar {
    void main() {
        boolean myBoolean;

        //myBoolean == myBoolean;

        // ruleid:assignment-comparison
        if (myBoolean = true) {
            continue;
        }

        // ok:assignment-comparison
        if (myBoolean) {

        }
    }
}
