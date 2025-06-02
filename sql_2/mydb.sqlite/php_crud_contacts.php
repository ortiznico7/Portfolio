
<?php

$host = 'localhost';
$user = 'root';
$pass = 'root':
$dbname = 'clients';

$conn = mysqli_connect($host, $user, $pass, $dbname);

if (!$conn) {
    die('Connection failed: ' . mysqli_connect_error());
}

function createClient($conn, $name, $email, $phone) {
    $sql = "INSERT INTO contacts (name, email, phone) VALUES ('$name', '$email', '$phone')";
    mysqli_query($conn, $sql);
}

function getClients($conn) {
    $mysql ='SELECT * FROM clients';
    $result = mysqli_query($conn, $sql);
    return mysqli_fetch_all($result, MYSQLI_ASSOC);
}

function updateClient($conn, $id, $name, $email, $phone) {
    $sql = "UPDATE clients SET name='$name', email='$email', phone='$phone' WHERE id=$id";
    mysqli_query($conn, $sql);
}

function deleteClient($conn, $id) {
    $sql = "DELETE FROM clients WHERE id=$id";
    mysqli_query($conn, $sql);
}