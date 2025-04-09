class Facteurs {
    public static int facteurs(int n) {
        if (n == 1) {
            return 0;
        }
        int p = 0;
        for (int i = 2; i < n; i++) {
            boolean isPrime = true;
            for (int j = 2; j < i; j++) {
                if (i % j == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) {
                p = i;
            }
        }
        return p;
    }
}
