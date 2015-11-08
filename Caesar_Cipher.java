import java.util.Scanner;

public class Caesar_Cipher {
	public static void main(String[] args){
		
	/*
	Problem Statement:
		Julius Caesar protected his confidential information from his enemies by encrypting it. 
		Caesar rotated every alphabet in the string by a fixed number K. 
		This made the string unreadable by the enemy.
		You are given a string S and the number K. 
		Encrypt the string and print the encrypted string.
		
		For example: 
		If the string is middle-Outz and K=2, the encoded string is okffng-Qwvb. 
		Note that only alphabets are encrypted while symbols like - are untouched. 
		'm' becomes 'o' when alphabets are rotated twice, 
		'i' becomes 'k', 
		'-' remains the same because only alphabets are encoded, 
		'z' becomes 'b' when rotated twice.
		
	Input Format:
		Input consists of an integer N equal to the length of the string, followed by the string S and an integer K.
		
	Constraints:
		1≤N≤100 
		0≤K≤100 
		S is a valid ASCII string and doesn't contain any spaces.
		
	Output Format:
		For each test case, print the encoded string.
		
	Sample Input:
		11
		middle-Outz
		2
		
	Sample Output:
		okffng-Qwvb
	 */
		
		
		Scanner in = new Scanner(System.in);
		
		int txtLength = Integer.parseInt(in.nextLine());
		String txtIn = in.nextLine();
		int offset = Integer.parseInt(in.nextLine());
		
		in.close();
		
		String alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz";
		String encrypted = "";
		
		int alphabetLength = alphabet.length() / 2;
		offset = offset % alphabetLength; 
		
		char[] text = txtIn.toCharArray();
		char[] alfa = alphabet.toCharArray();

		for (int i = 0; i < txtLength; i++){
			for (int j = 0; j < alphabetLength; j++){
				if (alfa[j] == text[i]){
					encrypted += alfa[j + offset];
					break;
				} 
				else if (Character.toUpperCase(alfa[j]) == text[i]){
					encrypted += Character.toUpperCase(alfa[j + offset]);
					break;
				} 
				else if(j == alphabetLength -1){
					encrypted += text[i];
				}
			}
		}
		
		System.out.println(encrypted);
	}
}
