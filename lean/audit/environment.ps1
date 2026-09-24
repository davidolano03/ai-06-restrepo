$env:PATH = 'C:\Users\Bienvenido\Documents\GitHub\ai-05-ide\.work\elan\toolchains\leanprover--lean4---v4.30.0-rc2\bin;' + $env:PATH
$env:PYTHONPATH = "$PWD;C:\Users\Bienvenido\Documents\GitHub\ai-05-ide\.work\python-compat"
$env:LEAN_NUM_THREADS='1'
$taskDeps = @(Get-ChildItem '.lake\packages' -Directory)
$env:GIT_CONFIG_COUNT = $taskDeps.Count
for ($taskI=0; $taskI -lt $taskDeps.Count; $taskI++) {
 [Environment]::SetEnvironmentVariable("GIT_CONFIG_KEY_$taskI", 'safe.directory', 'Process')
 [Environment]::SetEnvironmentVariable("GIT_CONFIG_VALUE_$taskI", ('C:/Users/Bienvenido/Documents/GitHub/ai-05-ide/.work/AppliedModelingLib/.lake/packages/' + $taskDeps[$taskI].Name), 'Process')
}
