export default function handleResponseFromAPI(promise) {
	return promise
		.then((response) => {
			console.log(response);
			return { status: 200, body: 'success' };
		}
		)
		.catch((error) => {
			console.log(error);
			return new Error();
		})
		.finally(() => {
			console.log('Got a response from the API');
		});
}
