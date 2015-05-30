<!DOCTYPE html>
<html>
<head>
<title>
Bottle framework using a template
</title>
</head>
<body>
<p>Here is the array that you sent me:</p>

<ol>
%for thing in things:
	<li>{{thing}}</li>
%end
</ol>

%if defined ('favthing'):
<p>Your favourite thing is {{favthing}}.</p>
%end

<p>What's your favourite thing?</p>
<form action="/fav" method="POST">
<input type=text name=favthing>
<input type=submit>
</form>

</body>
</html>
