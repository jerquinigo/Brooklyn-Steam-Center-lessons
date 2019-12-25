## Whitespaces and Indentation 
___

With other programming languages,indentation is used to help make code more readable. It helps show where blocks of code is located and the logic flow. It is not neccessary, but it is good practice. 

```javascript
import React from "react";
import "./CSS/DisplayResults.css";
const DisplayResults = props => {
	const { resData } = props;
	if (resData === "") return null;

	return resData.map((el, i) => {
		return (
			<div key={i} className="row">
				<div className="col s1 m1" />
				<div className="col s10 m10">
					<div className="card">
						<div className="card-image">
							<img src={el.data.url} alt="" />
						</div>
						<span className="card-title">{el.data.title}</span>

						<div className="card-content">
							<div className="display-override">
								<span>
									Date Created: {props.timeConverter(el.data.created)}
								</span>

								<span>Subreddit: {el.data.subreddit_name_prefixed}</span>

								<span>Score: {el.data.score}</span>

								<span>Ups: {el.data.ups}</span>

								<span>Comments: {el.data.num_comments}</span>
							</div>
						</div>
					</div>
				</div>
			</div>
		);
	});
};

export default DisplayResults;
```
Having code indented helps located where a bug can live and easier for troubleshooting. Whether you indent your code with other languages just as javascript, the code will compile and run either way. Same code below without indentation and it will return the same results.


```javascript
import React from "react";
import "./CSS/DisplayResults.css";
const DisplayResults = props => {
	const { resData } = props;
	if (resData === "") return null;

	return resData.map((el, i) => {
		return (
<div key={i} className="row">
<div className="col s1 m1" />
<div className="col s10 m10">
<div className="card">
<div className="card-image">
<img src={el.data.url} alt="" />
</div>
<span className="card-title">{el.data.title}</span>
<div className="card-content">
<div className="display-override">
<span>
Date Created: {props.timeConverter(el.data.created)}
</span>
<span>Subreddit: {el.data.subreddit_name_prefixed}</span>
<span>Score: {el.data.score}</span>
<span>Ups: {el.data.ups}</span>
<span>Comments: {el.data.num_comments}</span>
</div>
</div>
</div>
</div>
</div>
);
});
};

export default DisplayResults;
```


both blocks of code will return the same results. What if there was a bug, and your job was to find it and fix it. Which block of code would you want to work with? the organized one with proper indentation or the code that all on the left side? 

Progammers have standards for indentations to help make code more readable and makes their lives easier for debugging code that is not working. Other languages use syntax such curly braces to show where the start of a block of code begins and end

example:

```javascript
for(i = 0; i <= 100; i++){
    console.log(i)
}
```

the curly braces in this example show where the block of code for the for loop starts and ends. You can choose not to indent it and will still run and print you all the values up to and including 100. In Python, this will not work


Python does not have syntax to show where a block of code begins and ends. This is where whitespaces and indentation is crucial. Your program will not run if it does not have the mandatory indentation and whitespaces. Even if the logic is correct, Python will not know how to compile your code

example of good python code
```python
for i in range(1,101):
    print(i)
```

bad python code

```python
for i in range(1,101):
print(i)
```

This will not print, even though the logic is correct. Please keep this in mind where you would need to indent your code.

General guidelines for where to indent your code
* within your condition flow logic
* within your function
* for loops
* while loops
* nested blocks of code
