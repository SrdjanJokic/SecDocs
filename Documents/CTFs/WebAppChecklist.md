# Web App Checklist

## Description

Web Application Penetration Testing involves simulating cyberattacks against APIs and servers to identify vulnerabilities and/or exploit them. Here, we won't be mentioning port scanning or anything similar, just basic stuff we can do on a certain webpage or with a certain API.

## Tooling

This is a list of tools most commonly used in Web App Penetration Testing, along with their description:

|Tool|Description|
|---|---|
|[BurpSuite](../Tools/BurpSuite.md)|Allows full control over the interaction with the web app. Acts as a proxy and allows the HTTP(S) traffic to be intercepted, inspected and modified. Supports brute-force attacking (at a lower pace on free version) and decoding of responses.|
|[CyberChef](../Tools/CyberChef.md)|Simple-to-use web app for decoding and encoding various bits of data (such as base64 which is commonly seen in CTF challenges)|

## Checklist - Easy

These are the most obvious vulnerabilities found in easy CTF challenges. They are so obvious that you'll most likely skip this section every time you go through it, but for the sake of completion, we're still going to cover them here.

### Page Source contains flag or secret data

The name says it all. Sometimes you'll encounter the flag right in the page source, or you might find a comment accidentally left by a developer (such as SSH Private Keys, admin logins etc.). To exploit, simply inspect page source of a desired page and look for any info that shouldn't be there.

Hint: Sometimes although there is no secret data on this page, it might contain data that is never displayed. An example would be a value of users ID stored somewhere on the page, but never rendered. For example, if you were to find a value `ID = 21`, you could assume that to be the ID of the currently logged in user and attempt an IDOR attack.

`Right Click -> Developer Tools -> View Page Source`

### Reflected XSS Injection is allowed

If this is your first time facing this in a CTF challenge, or you simply can't remember how to pop this, refer to [OWASP XSS](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting) page for more info. Basically, send the request with the following somewhere where user info is excepted:

`<script>alert(123)</script>` or 
`“><script>alert(document.cookie)</script>`

If you see a JS alert somewhere on your page, it means XSS can be invoked and potentially exploited.

Hint: Some challenges will only ask you to pop an XSS, without actually trying to find a flag somewhere. The code above should provide fast results if that's the case.

### User can supply CMD input through request

Sometimes you'll notice that the website actually sends out a request containing a linux command. Usually, this would be to fetch a .txt file that it displays on page you're currently viewing. If you see something like `'cat /file.txt'` somewhere in the API call, chances are you can inject your own command and execute it on the server. An example you would want to try would be:

`';cat /flag'`. 

This simply ends the previous command and executes yours right after it. Another version of this would be that the server is actually not expecting an entire command, yet it's expecting an argument to a hardcoded command. For example, if the purpose of the webpage is to display time, it could be configured as such: `date -d $timeformat`. In this case, you can't simply forward an entire command because it will simply (fail `date -d ;cat /flag` is not a valid command). To get around this, provide the expected arguments, and use the `&&` symbols to concatenate an additional command. Such as: 

`4 aug 1995 10:10 am" +"%h %d %Y %H %M" && cat /flag && date -d "4 aug 1995 10:10 am""`

The code above will display the expected date along with the flag.

### No cookie validation

More often that not, these easy machines will use some sort of cookie for user authentication. These can *usually* be intercepted and modified in such a way that further requests contain more privileges than they should. For example, when hitting the `auth` endpoint, you might see a response in BurpSuite containing a header: `Set-Cookie: ewogICAidXNlcm5hbWUiOiJndWVzdCIKfQ==`. If you were to put this in CyberChef, you'd see that it's deserialized as:

```json
{
   "username":"guest"
}
```

If you were given a task where, let's say, you need to "gain Admin access", chances are we could simply modify this cookie with the admin username and hope that the server does no other validation at that point. So, by taking the following JSON

```json
{
   "username":"admin"
}
```

and putting it in CyberChef to encode it in base64, we'd see the output `ewogICAidXNlcm5hbWUiOiJhZG1pbiIKfQ==`. We can then send it as a cookie in the header and gain admin access to the website.

### IDOR

If this is your first time interacting with IDOR, you can read more about it [here](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/05-Authorization_Testing/04-Testing_for_Insecure_Direct_Object_References). One common mistake that I used to make is that I assumed that we could access any webpage without authentication. On these easy machines, access to a webpage is usually determined just by the existence of a cookie, not the actual permissions of the user stored within it. What this means is that we can probably view any page, just as long as we have **a** user, regardless of them being an admin or not. 

For example, hitting `https://www.foo.bar/dashboard?id=21` might yield a `403 Forbidden` if we have no cookie. However, if we have a cookie of a regular user and try hitting that again, we might just see a `200 OK` response instead.

Hint: When attempting various ID's, use BurpSuites Intruder functionality to send a lot of different ID's without having to type them manually. Also note, if the server is configured to return `200 OK` regardless of failed or successful authentication, sort by response size. Success and fail response size will usually vary, regardless of the response code.