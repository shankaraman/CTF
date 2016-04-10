for file in $(find . -type d -mindepth 1 -maxdepth 1); do
        cert="${file}/META-INF/CERT.RSA";

        [ -f $cert ] &&
        fgrep -q '@android.com' $cert ||
        fgrep -q 'Google, Inc'  $cert ||
        fgrep -q 'Google Inc'   $cert ||
        echo $file;
done
