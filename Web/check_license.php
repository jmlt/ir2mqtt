<?php
header("Content-Type: application/json");
require "db.php";

$data = json_decode(file_get_contents("php://input"), true);
$license = $data["license_key"] ?? "";

if (!$license) {
    http_response_code(400);
    echo json_encode(["success" => false, "error" => "Missing license_key"]);
    exit;
}

$stmt = $pdo->prepare("
    SELECT l.license_key, d.email, l.value, l.currency, l.origin, l.created_at
    FROM licenses l
    LEFT JOIN donors d ON l.donor_id = d.id
    WHERE l.license_key = ?
");
$stmt->execute([$license]);
$result = $stmt->fetch(PDO::FETCH_ASSOC);

if ($result) {
    echo json_encode(["success" => true, "license" => $result]);
} else {
    echo json_encode(["success" => false, "error" => "License not found"]);
}
?>
