// Branch, sub-branch and category types
// PSCApp/src/api/branch/serializers.py

export interface SubBranch {
  id: number;
  branch: number;
  name_en: string;
  name_np: string;
  slug: string;
  description_en: string | null;
  description_np: string | null;
  icon: string | null;
  display_order: number;
  is_active: boolean;
}

export interface Branch {
  id: number;
  name_en: string;
  name_np: string;
  slug: string;
  description_en: string | null;
  description_np: string | null;
  icon: string | null;
  has_sub_branches: boolean;
  sub_branches: SubBranch[];
  display_order: number;
  is_active: boolean;
}

export type CategoryScopeType = string; // e.g. "UNIVERSAL" | "BRANCH" | "SUB_BRANCH"
export type CategoryType = string; // e.g. "GENERAL" | "SPECIAL" | ...

export interface Category {
  id: number;
  name_en: string;
  name_np: string;
  slug: string;
  description_en: string | null;
  description_np: string | null;
  scope_type: CategoryScopeType;
  target_branch: number | null;
  target_branch_name: string | null;
  target_sub_branch: number | null;
  target_sub_branch_name: string | null;
  category_type: CategoryType;
  is_public: boolean;
  created_by: number | null;
  icon: string | null;
  color_code: string | null;
  display_order: number;
  is_active: boolean;
  question_count?: number;
}
