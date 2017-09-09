$cipher = "CHIPHER"

function crypt($input_text, $encrypt){

	if ($input_text.Length -lt $cipher.Length){
		Write "Text too short, make cipher shorter or the text longer"
		return
	}

	$input_text_array = $input_text.ToCharArray()
	$key_text_array = generate_cipher_text_array $input_text_array

	if ($encrypt){
		encrypt $input_text_array $key_text_array
	}
	else {
		decrypt $input_text_array $key_text_array
	}
}

function generate_cipher_text_array($input_text_array){
	$cipher_index = 0
	$counter = 0

	foreach($i in $input_text_array){
		$key_text = $key_text + $cipher[$cipher_index]
		$counter = $counter + 1 
		$cipher_index = $counter % $cipher.Length
	}

	return $key_text.ToCharArray()
}

function encrypt($input_text_array, $key_text_array){
	$output_text = ""
	$counter = 0

	foreach($_ in $input_text_array){
		$offset_char = [int]$input_text_array[$counter]
		$offset_char = $offset_char + [int]$key_text_array[$counter]
		$output_text = $output_text + [char]$offset_char
		$counter = $counter + 1  
	}

	write $output_text
}

function decrypt($input_text_array, $key_text_array){
	$output_text = ""
	$counter = 0

	foreach($_ in $input_text_array){
		$offset_char = [int]$input_text_array[$counter]
		$offset_char = $offset_char - [int]$key_text_array[$counter]
		$output_text = $output_text + [char]$offset_char
		$counter = $counter + 1  
	}

	write $output_text
}


$input_text = Read-Host "Write text to be encrypted or decrypted"
$crypt_option = Read-Host "write 'e' to encrypt, or 'd' to decrypt"

if ($crypt_option -eq "e"){
	crypt $input_text $true
}
elseif ($crypt_option -eq "d"){
	crypt $input_text $false
}
