package day02;

public class OopTest {
	public static void main(String[] args) {
		Human hum = new Human();
		System.out.println(hum.age);
		System.out.println(hum.language);
		hum.getOlder();
		hum.momstouch(7);
		System.out.println(hum.age);
		System.out.println(hum.language);
		
	}
}
