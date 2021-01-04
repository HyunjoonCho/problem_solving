package javalang;

class ArrayCopyTest {
    public static void main(String[] args) {
        int[] array = {1, 2};
        System.out.println(array[0]);
        modify(array);
        System.out.println(array[0]);
    }    

    public static void modify(int[] array) {
        array[0] = 3;
    }
}
