class VarWildcard {
    public static int foo(int x) {
        x = 1;
        int y = 1;
        int res = x + y;
        double x2 = 1.0;
        double y2 = 1.0;
        double res2 = x2 + y2;
        return res;
    }
}
