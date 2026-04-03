import { useState, useEffect } from 'react';
import { fetchTasks, createTask, updateTask, logSession } from '../api';

export default function Dashboard() {
  const [tasks, setTasks] = useState([]);
  const [newTask, setNewTask] = useState('');

  useEffect(() => { fetchTasks().then(res => setTasks(res.data)); }, []);

  const addTask = async () => {
    if (!newTask.trim()) return;
    const res = await createTask(newTask);
    setTasks(prev => [res.data, ...prev]);
    setNewTask('');
  };

  const toggleComplete = async (task) => {
    await updateTask(task.id, { completed: !task.completed });
    setTasks(prev => prev.map(t => t.id === task.id ? { ...t, completed: !t.completed } : t));
  };

  const focus = async (task) => {
    await logSession(task.id, 25);
    alert(`✅ Logged 25m focus for "${task.title}"`);
  };

  return (
    <div style={{ maxWidth: 600, margin: '2rem auto', fontFamily: 'sans-serif' }}>
      <h1>FocusFlow</h1>
      <div style={{ display: 'flex', gap: 8, marginBottom: '1rem' }}>
        <input value={newTask} onChange={e => setNewTask(e.target.value)} placeholder="New task..." style={{ flex: 1, padding: 8 }} />
        <button onClick={addTask}>Add</button>
      </div>
      <ul style={{ listStyle: 'none', padding: 0 }}>
        {tasks.map(t => (
          <li key={t.id} style={{ display: 'flex', alignItems: 'center', gap: 8, padding: '8px 0', borderBottom: '1px solid #eee' }}>
            <input type="checkbox" checked={t.completed} onChange={() => toggleComplete(t)} />
            <span style={{ textDecoration: t.completed ? 'line-through' : 'none', flex: 1 }}>{t.title} ({t.total_focus_minutes}m focused)</span>
            <button onClick={() => focus(t)} disabled={t.completed}>Focus 25m</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
