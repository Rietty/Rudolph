-- Advent of Code - Repository-local Neovim configuration

local M = {}

-- Configuration
local TEMPLATE = "src/solutions/template.py"
local APP = "src/app.py"

local function project_root()
	return vim.fs.root(0, { "pyproject.toml", ".git" }) or vim.fn.getcwd()
end

-- Get year/day from current file path
local function get_current_day()
	local file = vim.api.nvim_buf_get_name(0)

	local year, day = file:match("[/\\]y(%d+)[/\\]day(%d+)%.py$")

	if year and day then
		return year, tonumber(day)
	end

	return nil, nil
end

-- Ask for year and day when they cannot be inferred
local function get_aoc_date(callback)
	local year, day = get_current_day()

	if year and day then
		callback(year, day)
		return
	end

	vim.ui.input({ prompt = "Year: " }, function(input_year)
		if not input_year or not input_year:match("^%d%d%d%d$") then
			return
		end

		vim.ui.input({ prompt = "Day: " }, function(input_day)
			local parsed_day = tonumber(input_day)

			if not parsed_day or parsed_day < 1 or parsed_day > 25 then
				return
			end

			callback(input_year, parsed_day)
		end)
	end)
end

-- Create a new day's solution
function M.create_day()
	local root = project_root()

	local template = root .. "/" .. TEMPLATE

	if vim.fn.filereadable(template) == 0 then
		vim.notify("Template not found: " .. TEMPLATE, vim.log.levels.ERROR)
		return
	end

	get_aoc_date(function(year, day)
		local day_padded = string.format("%02d", day)

		local destination_dir = string.format("%s/src/solutions/y%s", root, year)

		local destination = string.format("%s/day%s.py", destination_dir, day_padded)

		vim.fn.mkdir(destination_dir, "p")

		local contents = vim.fn.readfile(template)

		if vim.fn.writefile(contents, destination) ~= 0 then
			vim.notify("Failed to create solution", vim.log.levels.ERROR)
			return
		end

		vim.notify("Created " .. destination, vim.log.levels.INFO)

		vim.cmd("edit " .. vim.fn.fnameescape(destination))
	end)
end

-- Run Advent of Code solution
function M.run()
	local root = project_root()

	get_aoc_date(function(year, day)
		vim.ui.select({ "a", "b" }, {
			prompt = "Select Advent of Code part:",
		}, function(part)
			if not part then
				return
			end

			vim.ui.select({
				"Run",
				"Test",
				"Submit",
			}, {
				prompt = "Select execution mode:",
			}, function(mode)
				if not mode then
					return
				end

				local args = {
					"uv",
					"run",
					APP,
					"-y",
					year,
					"-d",
					string.format("%02d", day),
					"-p",
					part,
				}

				if mode == "Test" then
					table.insert(args, "-t")
				elseif mode == "Submit" then
					table.insert(args, "-s")
				end

				-- Open terminal split
				vim.cmd("botright 15new")

				vim.fn.termopen(args, {
					cwd = root,
				})

				vim.cmd("startinsert")
			end)
		end)
	end)
end

-- Keybindings
vim.keymap.set("n", "<leader>an", M.create_day, {
	desc = "AoC: Create new day",
})

vim.keymap.set("n", "<leader>ar", M.run, {
	desc = "AoC: Run solution",
})

return M
