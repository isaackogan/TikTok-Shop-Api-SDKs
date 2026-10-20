<?php
// Router for PHP's built-in web server (see ServerTest). Logs every request as a JSON line to $STUB_LOG, then:
//   /redirect/...  -> 302 to /target/secret on the same server
//   /sleep/...     -> answers after 3 seconds
//   anything else  -> a success envelope
declare(strict_types=1);

$uri = $_SERVER['REQUEST_URI'];
$path = parse_url($uri, PHP_URL_PATH) ?: '/';
$log = getenv('STUB_LOG');
if ($log) {
    file_put_contents($log, json_encode([
        'method' => $_SERVER['REQUEST_METHOD'],
        'uri' => $uri,
        'path' => $path,
        'headers' => getallheaders(),
        'body' => file_get_contents('php://input'),
    ]) . "\n", FILE_APPEND | LOCK_EX);
}

header('Content-Type: application/json');
if (str_starts_with($path, '/redirect')) {
    http_response_code(302);
    header('Location: http://' . $_SERVER['HTTP_HOST'] . '/target/secret');
    return;
}
if (str_starts_with($path, '/sleep')) {
    sleep(3);
}
echo json_encode(['code' => 0, 'message' => 'Success', 'request_id' => 'req-live', 'data' => new stdClass()]);
