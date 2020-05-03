/* part one: 
This code is supposed to calculated pay, and taxes
*/

class ch9{
	public static void main(String[] args) {
		double hours_worked = 30; //hour 
		double pay_per_hour = 10; //dollar amount
		double tax_rate = 0.1; 
		double taxes = hours_worked * pay_per_hour * tax_rate;

		System.out.println("When you're paid " + pay_per_hour
			+ "$, and you work " + hours_worked + " hours per week" +
			" ,you have to pay " + taxes + "$ in taxes.");
	}
}