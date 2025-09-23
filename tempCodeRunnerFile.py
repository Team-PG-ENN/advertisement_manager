ui.add_head_html("""
<style>
@keyframes typing-loop {
  0% { width: 0; }
  40% { width: 100%; }
  90% { width: 100%; }
  100% { width: 0; }
}

.typewriter {
  display: inline-block;
  overflow: hidden;
  white-space: nowrap;
  width: 0;
  animation: typing-loop 7s steps(12, end) infinite;
}
</style>
""")