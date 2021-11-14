import java.util.Scanner;
class FamilyAccount
{
	public static void main(String[] args)
	{
		int balance=0;
		String details = "收支\t账户金额\t收支金额\t说明\n"; 
		boolean isFlag=true;
		while(isFlag)
		{
			System.out.println("-----------------家庭收支记账软件-----------------\n"); 
			System.out.println("                   1.收支明细"); 
			System.out.println("                   2.登记收入"); 
			System.out.println("                   3.登记支出"); 
			System.out.println("                   4.退出"); 
			System.out.print("\n                       请选择<1-4>：");
			Scanner scan = new Scanner(System.in);
			
			String id =scan.next();
			char idc=id.charAt(0); 
			while(idc!='1'&&idc!='2'&&idc!='3'&&idc!='4')
			{
				System.out.print("输入错误，请重新输入：");
				id =scan.next();
				idc=id.charAt(0); 
			}
			
			switch(idc)
			{
				case '1':
					System.out.println("1.收支明细");
					System.out.println("-----------------当前收支明细记录-----------------");
					System.out.println(details); 
					System.out.println("--------------------------------------------------");
					break;
				case '2':
				    System.out.println("2.登记收入"); 
				    System.out.print("本次收入金额："); 
				    int money = scan.nextInt();
				    System.out.print("本次收入说明：");
					String info = scan.next(); 
					balance += money;
					details += ("收入\t"+balance+"\t\t"+money+"\t\t"+info+"\n");
					System.out.println("-----------------登记完成-----------------\n");
				    break;
				case '3':
					System.out.println("3.登记支出"); 
					System.out.print("本次支出金额："); 
				    money = scan.nextInt();
				    System.out.print("本次支出说明：");
					info = scan.next(); 
					balance += money;
					details += ("支出\t"+balance+"\t\t"+money+"\t\t"+info+"\n");
					System.out.println("-----------------登记完成-----------------\n");
				    break;
				case '4':
				    System.out.print("你确定？(y/n)：");
			        String out =scan.next();
			        char outc=out.charAt(0); 
			        while(outc!='y'&&outc!='n')
			        {
			          	System.out.print("输入错误，请重新输入：");
			         	out =scan.next();
				        outc=out.charAt(0); 
			        }
			        if(outc=='y')
			        {
			        	isFlag=false;
					}
				    break;
			}
		}
		
	}
}