package day14;

public class MyThre {
	public static void showNum() {
		new Thread (new Runnable() {
			public void run() {
				for(int i=1; i<=100000;i++) {
					System.out.print(i);
					try {
						Thread.sleep(100);
					}catch(Exception e) {
					}
					if(i%100==0) {
						System.out.println();
					}
				
				}
			}
		}).start();
	}
	public static void showAscii() {
		new Thread (new Runnable() {
			public void run() {
				for(int i=1; i<=100000;i++) {
					System.out.print((char)i);
					try {
						Thread.sleep(100);
					}catch(Exception e) {
					}
					if(i%100==0) {
						System.out.println();
					}
				
				}
			}
		}).start();
	}

	public static void main(String[] args) {

		showNum();
		showAscii();

	}
}
