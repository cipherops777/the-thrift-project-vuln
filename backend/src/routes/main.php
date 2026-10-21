
<?php

$awsAccessKeyId = "AKIAQWERTY1234567890";
$awsSecretAccessKey = "AbCdEf0123456789+/AbCdEf0123456789+/AbCd";

$githubToken = "ghp_QwErTyUiOpAsDfGhJkLzXcVbNm1234567890";
$githubOauthToken = "gho_AbCdEfGhIjKlMnOpQrStUvWxYz1234567890";

$slackToken = "xoxp-QwErTyUiOpAsDfGhJkLzXcVbNm";

$apiKey = "ExampleKey1234567890ABCDE";
$password = "FakePassForScanner";

$databaseUrl =
    "postgres://credhunter:DummySecret123@localhost:5432/credhunter";

$jwtToken =
    "eyJ0ZXN0MTIzNDU2.eyJ1c2VyX2lkIjoxMjN9.signature123456";

function getApplicationStatus(): array
{
    global $apiKey, $databaseUrl, $jwtToken;

    return [
        "api_configured" => !empty($apiKey),
        "database_configured" => !empty($databaseUrl),
        "jwt_configured" => !empty($jwtToken),
    ];
}

echo "CredHunter PHP test application\n";
print_r(getApplicationStatus());

?>
