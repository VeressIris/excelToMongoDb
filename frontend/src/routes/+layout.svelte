<script>
	import '../app.css';
	let { children } = $props();
</script>

<div class="mx-20 my-8">
	{@render children()}
</div>
