import java.util.Scanner;
class FamilyAccount
{
	public static void main(String[] args)
	{
		int balance=0;
		String details = "��֧\t�˻����\t��֧���\t˵��\n"; 
		boolean isFlag=true;
		while(isFlag)
		{
			System.out.println("-----------------��ͥ��֧�������-----------------\n"); 
			System.out.println("                   1.��֧��ϸ"); 
			System.out.println("                   2.�Ǽ�����"); 
			System.out.println("                   3.�Ǽ�֧��"); 
			System.out.println("                   4.�˳�"); 
			System.out.print("\n                       ��ѡ��<1-4>��");
			Scanner scan = new Scanner(System.in);
			
			String id =scan.next();
			char idc=id.charAt(0); 
			while(idc!='1'&&idc!='2'&&idc!='3'&&idc!='4')
			{
				System.out.print("����������������룺");
				id =scan.next();
				idc=id.charAt(0); 
			}
			
			switch(idc)
			{
				case '1':
					System.out.println("1.��֧��ϸ");
					System.out.println("-----------------��ǰ��֧��ϸ��¼-----------------");
					System.out.println(details); 
					System.out.println("--------------------------------------------------");
					break;
				case '2':
				    System.out.println("2.�Ǽ�����"); 
				    System.out.print("���������"); 
				    int money = scan.nextInt();
				    System.out.print("��������˵����");
					String info = scan.next(); 
					balance += money;
					details += ("����\t"+balance+"\t\t"+money+"\t\t"+info+"\n");
					System.out.println("-----------------�Ǽ����-----------------\n");
				    break;
				case '3':
					System.out.println("3.�Ǽ�֧��"); 
					System.out.print("����֧����"); 
				    money = scan.nextInt();
				    System.out.print("����֧��˵����");
					info = scan.next(); 
					balance += money;
					details += ("֧��\t"+balance+"\t\t"+money+"\t\t"+info+"\n");
					System.out.println("-----------------�Ǽ����-----------------\n");
				    break;
				case '4':
				    System.out.print("��ȷ����(y/n)��");
			        String out =scan.next();
			        char outc=out.charAt(0); 
			        while(outc!='y'&&outc!='n')
			        {
			          	System.out.print("����������������룺");
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